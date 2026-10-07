// Prints a new VAPID key pair for web push (owner step). Put VAPID_PUBLIC_KEY in Netlify as VITE_VAPID_PUBLIC_KEY and
// in function secrets; put VAPID_PRIVATE_KEY only in function secrets. Never commit the private key.
const k = await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits'])
const pub = Buffer.from(await crypto.subtle.exportKey('raw', k.publicKey)).toString('base64url')
const { d } = await crypto.subtle.exportKey('jwk', k.privateKey)
console.log(`VAPID_PUBLIC_KEY=${pub}\nVAPID_PRIVATE_KEY=${d}`)
