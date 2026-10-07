// Tiny local stand-in for the Supabase gateway, for development only:
//   /rest/v1/<path>  → PostgREST at <path>
//   GET /auth/v1/user → the user in a locally signed JWT (HS256, LOCAL_JWT_SECRET), the one Auth call clients
//                       make to validate a session. No sign-up, passwords or email: tests mint tokens directly.
import http from 'node:http'
import { createHmac, timingSafeEqual } from 'node:crypto'

const [listen, upstream] = process.argv.slice(2).map(Number)
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': 'GET,POST,PATCH,PUT,DELETE,OPTIONS' }

function verify(token) {
  const [h, p, sig] = (token ?? '').split('.')
  if (!h || !p || !sig) return null
  const want = createHmac('sha256', SECRET).update(`${h}.${p}`).digest('base64url')
  if (want.length !== sig.length || !timingSafeEqual(Buffer.from(want), Buffer.from(sig))) return null
  const claims = JSON.parse(Buffer.from(p, 'base64url').toString('utf8'))
  if (claims.exp && claims.exp * 1000 < Date.now()) return null
  return claims
}

http
  .createServer((req, res) => {
    if (req.method === 'OPTIONS') {
      res.writeHead(204, CORS)
      return res.end()
    }
    if ((req.url ?? '').startsWith('/auth/v1/user')) {
      const claims = verify((req.headers.authorization ?? '').replace(/^Bearer /, ''))
      if (!claims?.sub) {
        res.writeHead(401, { ...CORS, 'content-type': 'application/json' })
        return res.end(JSON.stringify({ code: 401, msg: 'invalid JWT' }))
      }
      res.writeHead(200, { ...CORS, 'content-type': 'application/json' })
      return res.end(
        JSON.stringify({ id: claims.sub, aud: 'authenticated', role: 'authenticated', email: claims.email ?? null, app_metadata: {}, user_metadata: {}, created_at: new Date(0).toISOString() }),
      )
    }
    const path = (req.url ?? '/').replace(/^\/rest\/v1/, '') || '/'
    const headers = { ...req.headers, host: `127.0.0.1:${upstream}` }
    delete headers.apikey
    const up = http.request({ host: '127.0.0.1', port: upstream, path, method: req.method, headers }, (r) => {
      res.writeHead(r.statusCode ?? 502, { ...r.headers, 'access-control-allow-origin': '*' })
      r.pipe(res)
    })
    up.on('error', () => {
      res.writeHead(502)
      res.end('upstream unavailable')
    })
    req.pipe(up)
  })
  .listen(listen, '127.0.0.1')
