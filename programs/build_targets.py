"""Builds programs/targets/{TN,OR}.json from the IPEDS registry and reviewed catalog configurations.

Catalog configurations below were set by reviewing what the program-depth runs retrieved from official hosts
(see each run's manifest). Seeds and hosts are retrieval starting points only; no fact is taken from them.
Run: python -m programs.build_targets
"""
import json
from pathlib import Path
R=Path(__file__).resolve().parent.parent
def reg(st): return {i['folder']:i for i in json.load(open(R/f'pipeline/registry/{st}.json'))['institutions'] if i['level']=='four_year'}

def acalog(host,catoid,lists): return {'platform':'acalog','home':f'https://{host}/index.php?catoid={catoid}','catoid':catoid,
    'program_lists':[f'https://{host}/content.php?catoid={catoid}&navoid={n}' for n in lists]}
def smart(host,prefix,lists=('programs-of-study',),min_depth=1): return {'platform':'smartcatalog','home':f'https://{host}{prefix}','path_prefix':prefix,'min_depth':min_depth,
    'program_lists':[f'https://{host}{prefix}{l}' for l in lists]}

TN={
 'utk':dict(priority=1,catalog=acalog('catalog.utk.edu',56,[12035]),policy=[
   'https://admissions.utk.edu/apply/first-year/college-admission-requirements/','https://haslam.utk.edu/admissions/',
   'https://nursing.utk.edu/admissions-and-aid/undergrad-admissions/','https://studentsuccess.utk.edu/career/university-exploratory-advising/',
   'https://tickle.utk.edu/access/expanding/scholarships/','https://tickle.utk.edu/','https://haslam.utk.edu/scholarships/']),
 'mtsu':dict(priority=1,catalog=acalog('catalog.mtsu.edu',49,[12728,12850,12870]),policy=[
   'https://nursing.mtsu.edu/future-bsn-students/','https://university-college.mtsu.edu/advising_undecided_chooseyourmajor/',
   'https://csc.mtsu.edu/scholarships/','https://jones.mtsu.edu/scholarships/','https://www.mtsu.edu/engineering/'],
   degree_maps=[], degree_map_link=r'catalog\.mtsu\.edu/mime/media/view/49/\d+',
   map_sources={'lists':['https://www.mtsu.edu/programs/','https://www.mtsu.edu/ucat/'],'page_link':r'www\.mtsu\.edu/programs?/[a-z0-9-]+/?$'}),
 'memphis':dict(priority=1,catalog=acalog('catalog.memphis.edu',43,[3163,3164,3170,3180]),policy=[
   'https://www.memphis.edu/aac/prepare/faqs.php','https://www.memphis.edu/fcbeundergrad/programs/bba-requirements.php',
   'https://www.memphis.edu/herff/future-students/orientation.php','https://www.memphis.edu/herff/students/scholarships.php',
   'https://www.memphis.edu/me/program/undergraduate/bsme_requirement.php','https://www.memphis.edu/nursing/program-admit/bsn/bsnadmissions.php',
   'https://www.memphis.edu/fcbescholarships/scholarships/undergraduate/freshmen-1.php'],
   degree_maps=['https://www.memphis.edu/cas/advising/degree_sheets.php'], degree_map_any_pdf=True),
 'tntech':dict(priority=1,render='browser',catalog={'platform':'coursedog','home':'https://undergrad.catalog.tntech.edu/','path_prefix':'/programs/','min_depth':0,
   'program_lists':['https://undergrad.catalog.tntech.edu/programs','https://undergrad.catalog.tntech.edu/ugrequirements/majors']
     +[f'https://undergrad.catalog.tntech.edu/programs?page={n}&pq=&sortBy=name' for n in range(2,13)]},
   policy=['https://www.tntech.edu/admissions/freshmen/index.php','https://www.tntech.edu/business/scholarships.php','https://www.tntech.edu/cis/undecided_majors.php',
   'https://www.tntech.edu/engineering/programs/csc/undergraduate-program.php','https://www.tntech.edu/engineering/programs/index.php',
   'https://www.tntech.edu/nursing/bsn-program.php','https://www.tntech.edu/sacscoc/academic_program_inventory.php','https://www.tntech.edu/engineering/admissions.php'],
   degree_maps=['https://www.tntech.edu/engineering/programs/index.php','https://www.tntech.edu/advisement/degree-maps.php']),
 'utc':dict(priority=1,catalog=acalog('catalog.utc.edu',53,[2300,2301,2302]),policy=[
   'https://www.utc.edu/academic-affairs/registrar/change-requests','https://www.utc.edu/college-of-nursing/bachelor-of-science-nursing/bsn-admission',
   'https://www.utc.edu/engineering-and-computer-science/center-for-student-success/student-organizations/scholarships-available',
   'https://www.utc.edu/enrollment-management-and-student-affairs/center-for-academic-support-and-advisement/academic-exploration/undecided-majors',
   'https://www.utc.edu/gary-w-rollins-college-of-business/student-resources/scholarships/general-scholarships'],
   degree_maps=['https://www.utc.edu/enrollment-management-and-student-affairs/advisement/advising-resources/clear-paths-for-advising/clear-paths-for-advising-2026-2027'],
   degree_map_any_pdf=True),
 'etsu':dict(priority=1,catalog=acalog('catalog.etsu.edu',65,[4652]),policy=[
   'https://www.etsu.edu/cas/applied-design/engineering/faq.php','https://www.etsu.edu/cas/applied-design/scholarship.php',
   'https://www.etsu.edu/cbat/management-supply-chain/documents/special_admission_requirements.pdf','https://www.etsu.edu/cbat_scholarships/',
   'https://www.etsu.edu/nursing/prospective_students/','https://www.etsu.edu/uac/undecided.php']),
 'apsu':dict(priority=2,render='browser',catalog={'platform':'coursedog','home':'https://undergraduate.catalog.apsu.edu/','path_prefix':'/programs/','min_depth':0,
   'program_lists':['https://undergraduate.catalog.apsu.edu/programs','https://undergraduate.catalog.apsu.edu/academics/programsbycollege']},
   policy=['https://www.apsu.edu/business/programs/apply-bba.php','https://www.apsu.edu/cpos/changeofmajor.php','https://www.apsu.edu/csci/b_s_degrees/',
   'https://www.apsu.edu/nursing/bachelornursing/bsn_criteria.php','https://www.apsu.edu/psychology/undergrad.php',
   'https://www.apsu.edu/student-success/college-success/academic-focus.php']),
 'utm':dict(priority=2,catalog=acalog('catalog.utm.edu',26,[722,729]),policy=[
   'https://www.utm.edu/academics/departments/engineering','https://www.utm.edu/academics/majors-and-programs/nursing-(pre-licensure-bsn)']),
 'tnstate':dict(priority=2,catalog=acalog('catalog.tnstate.edu',17,[963]),policy=[
   'https://www.tnstate.edu/aarc/undecided/','https://www.tnstate.edu/engineering/degrees.aspx','https://www.tnstate.edu/engineering/scholarships.aspx',
   'https://www.tnstate.edu/psychology/bspsych.aspx'],degree_maps=['https://www.tnstate.edu/academic_affairs/undergraduate_degree_programs.aspx']),
 'utsouthern':dict(priority=3,catalog=smart('utsouthern.smartcatalogiq.com','/en/2025-2026/undergraduate-catalog/'),
   discover=['https://utsouthern.smartcatalogiq.com/'],policy=['https://utsouthern.edu/academics/majors-and-programs/',
   'https://utsouthern.edu/academics/professional-studies/nursing-and-health-sciences/nursing/']),
 'vanderbilt':dict(priority=1,render='browser',catalog={'platform':'kuali','home':'https://www.vanderbilt.edu/catalogs/kuali/undergraduate-26-27','path_prefix':'/catalogs/','min_depth':5,'program_lists':[]},
   policy=['https://admissions.vanderbilt.edu/academics/','https://as.vanderbilt.edu/undergraduate-programs/majors-minors/','https://engineering.vanderbilt.edu/academics/Undergraduate/',
   'https://engineering.vanderbilt.edu/undergraduate-admissions/','https://computing.vanderbilt.edu/undergraduate-programs/','https://nursing.vanderbilt.edu/programs/prenursing/',
   'https://registrar.vanderbilt.edu/intra-university-transfers/index.php','https://business.vanderbilt.edu/business-minor/',
   'https://registrar.vanderbilt.edu/documents/Undergraduate-Catalog-2025-26.pdf']),
 'belmont':dict(priority=1,catalog=acalog('catalog.belmont.edu',21,[1170]),policy=[
   'https://belmont.edu/academics/undeclared.html','https://www.belmont.edu/academics/majors-programs/computer-science/','https://www.belmont.edu/academics/majors-programs/nursing/',
   'https://www.belmont.edu/registrar/advising-degree/change-of-major.html','https://www.belmont.edu/massey/']),
 'lipscomb':dict(priority=1,catalog=acalog('catalog.lipscomb.edu',33,[2730]),policy=[
   'https://lipscomb.edu/academics/programs/computer-science','https://lipscomb.edu/academics/programs/nursing',
   'https://lipscomb.edu/admissions/freshmen-admissions/scholars-programs/college-business-swang-scholars-program',
   'https://lipscomb.edu/admissions/freshmen-admissions/scholars-programs/raymond-b-jones-engineering-scholars-program','https://lipscomb.edu/engineering/engineering-scholarship',
   'https://www.lipscomb.edu/engineering/academic-programs/prospective-students','https://lipscomb.edu/one-stop/registrar-faqs']),
 'cn':dict(priority=2,render='browser',catalog={'platform':'coursedog','home':'https://catalog.cn.edu/','path_prefix':'/programs/','min_depth':0,
   'program_lists':['https://catalog.cn.edu/programs']},policy=['https://catalog.cn.edu/academic-policies','https://catalog.cn.edu/admissions']),
 'lanecollege':dict(priority=3,render='browser',catalog={'platform':'coursedog','home':'https://catalog.lanecollege.edu/','path_prefix':'/programs/','min_depth':0,
   'program_lists':['https://catalog.lanecollege.edu/programs']},policy=['https://catalog.lanecollege.edu/academics/academic-regulations']),
 'cbu':dict(priority=1,catalog=smart('cbu.smartcatalogiq.com','/en/2026-2027/catalog/',min_depth=1),policy=[
   'https://www.cbu.edu/academics/undergraduate-programs/electrical-engineering/','https://www.cbu.edu/academics/undergraduate-programs/traditional-bsn-nursing-program/',
   'https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/','https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/pascal-fellowship']),
 'rhodes':dict(priority=2,catalog={'platform':'drupal','home':'https://catalog.rhodes.edu/','program_link':r'catalog\.rhodes\.edu/programs-study/[^/?#]+/[^/?#]+$',
   'program_lists':['https://catalog.rhodes.edu/programs-study']},
   policy=['https://www.rhodes.edu/program-classifications','https://catalog.rhodes.edu/educational-program/academic-partnerships',
   'https://catalog.rhodes.edu/educational-program/requirements-degree','https://www.rhodes.edu/sites/default/files/Rhodes_College_Catalog_2026-27.pdf']),
 'uu':dict(priority=2,catalog=smart('uu.smartcatalogiq.com','/en/2026/2026-27-undergraduate-catalogue/',('academic-program/undergraduate-academic-programs','academic-program')),
   policy=['https://www.uu.edu/academics/departments/engineering/','https://www.uu.edu/academics/programs-of-study/computer-science/']),
 'leeuniversity':dict(priority=2,catalog=acalog('catalog.leeuniversity.edu',23,[34328,33249,33424]),policy=[
   'https://www.leeuniversity.edu/academics/nursing/admission/','https://www.leeuniversity.edu/academics/school-of-engineering/program/',
   'https://www.leeuniversity.edu/financial-aid/scholarships/','https://www.leeuniversity.edu/wp-content/uploads/Academic-Advising-Handbook.pdf']),
}
OR={
 'oregonstate':dict(priority=1,catalog={'platform':'courseleaf','home':'https://catalog.oregonstate.edu/','path_prefix':'/college-departments/','min_depth':1,
   'program_lists':['https://catalog.oregonstate.edu/programs/']},
   policy=['https://admissions.oregonstate.edu/uesp','https://catalog.oregonstate.edu/college-departments/engineering/',
   'https://catalog.oregonstate.edu/college-departments/business/','https://catalog.oregonstate.edu/regulations/regulations.pdf',
   'https://engineering.oregonstate.edu/about/curriculum-reform','https://engineering.oregonstate.edu/tools-services/how-to-pay-for-college/undergrad-scholarships',
   'https://engineering.oregonstate.edu/tools-services/financial-support/scholarships/catalyst-scholars-program','https://admissions.oregonstate.edu/first-year-admission-requirements']),
 'uoregon':dict(priority=1,catalog={'platform':'courseleaf','home':'https://catalog.uoregon.edu/','path_prefix':'/','min_depth':1,
   'program_lists':['https://catalog.uoregon.edu/ug-programs/']},
   policy=['https://advising.uoregon.edu/content/choose-your-major','https://business.uoregon.edu/programs/undergraduate/apply',
   'https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/lundquist-scholarships',
   'https://business.uoregon.edu/programs/undergraduate/apply/standard-admission/full-major-status','https://cs.uoregon.edu/undergraduate']),
 'pdx':dict(priority=1,catalog=smart('pdx.smartcatalogiq.com','/en/2026-2027/bulletin/'),policy=[
   'https://www.pdx.edu/advising/exploring-changing-majors','https://www.pdx.edu/business/undergrad-degree-requirements','https://www.pdx.edu/business/undergrad-funding',
   'https://www.pdx.edu/computer-science/undergraduate-admission','https://www.pdx.edu/engineering/scholarships-funding','https://www.pdx.edu/registration/major-change',
   'https://www.pdx.edu/engineering/upper-division-admissions','https://www.pdx.edu/psychology/program-details-psychology-babsminor'],
   degree_maps=['https://www.pdx.edu/registration/degree-maps'],degree_map_link=r'pdx\.edu/registration/.+-degree-map'),

 'linfield':dict(priority=2,catalog={'platform':'courseleaf','home':'https://catalog.linfield.edu/','program_link':r'catalog\.linfield\.edu/programs-az/(.+-major/(index\.html)?|nursing/)$',
   'program_lists':['https://catalog.linfield.edu/programs-az/']},policy=['https://www.linfield.edu/academics/nursing/index.html','https://www.linfield.edu/academics/business/index.html']),
 'lclark':dict(priority=2,catalog={'platform':'courseleaf','home':'https://docs.lclark.edu/undergraduate/','path_prefix':'/undergraduate/','min_depth':1,
   'program_lists':['https://docs.lclark.edu/undergraduate/policiesprocedures/majorsminors/'],
   'major_table':'https://docs.lclark.edu/undergraduate/policiesprocedures/majorsminors/',
   'award_statement':{'url':'https://docs.lclark.edu/undergraduate/graduationrequirements/requirements/','quote':'Undergraduate work at Lewis & Clark leads to the bachelor of arts degree','credential':'bachelor'}},
   policy=['https://college.lclark.edu/academics/pre_professional/engineering/','https://college.lclark.edu/academics/pre_professional/business_mba/']),
 'willamette-210401':dict(priority=2,render='browser',catalog={'platform':'coursedog','home':'https://catalog.willamette.edu/','path_prefix':'/programs/','min_depth':0,
   'program_lists':['https://catalog.willamette.edu/programs']},policy=['https://willamette.edu/academics/all-programs?programTypes=undergraduate']),
 'georgefox':dict(priority=1,catalog={'platform':'drupal','home':'https://www.georgefox.edu/catalog/index.html','program_link':r'georgefox\.edu/catalog/undergrad/curriculum/major_minor/[a-z_]+_major(_[a-z]+)?\.html$',
   'program_lists':['https://www.georgefox.edu/catalog/undergrad/curriculum/major_minor/index.html']},
   policy=['https://www.georgefox.edu/college-admissions/academics/major/index.html','https://www.georgefox.edu/college-admissions/academics/major/engineering.html',
   'https://www.georgefox.edu/college-admissions/academics/major/nursing.html'],discover=['https://www.georgefox.edu/catalog/index.html']),
 'eou':dict(priority=2,catalog=acalog('catalog.eou.edu',8,[463]),degree_maps=['https://catalog.eou.edu/content.php?catoid=8&navoid=475'],degree_map_any_pdf=True,
   policy=['https://www.eou.edu/academics/on-campus-majors-and-minors/']),
 'sou':dict(priority=2,catalog=acalog('catalog.sou.edu',18,[]),policy=['https://sou.edu/academics/?_degree_facet=major']),
 'up':dict(priority=1,catalog={'platform':'smartcatalog','home':'https://up.smartcatalogiq.com/en','path_prefix':'/en/2026-2027/','min_depth':2,
   'program_lists':['https://up.smartcatalogiq.com/en/2026-2027/bulletin/university-academic-programs-of-study/undergraduate-programs'],
   'printed_list':{'url':'https://up.smartcatalogiq.com/en/2026-2027/bulletin/university-academic-programs-of-study/undergraduate-programs','heading':'Undergraduate Programs','stop':'Up one level'}},
   discover=['https://up.smartcatalogiq.com/en'],policy=[]),
 'osucascades':dict(priority=2,catalog={'platform':'courseleaf','home':'https://catalog.oregonstate.edu/','path_prefix':'/college-departments/','min_depth':1,
   'program_lists':['https://catalog.oregonstate.edu/programs/'],'list_filter':'OSU-Cascades'},caps={'program_page':0},
   policy=['https://osucascades.edu/academics']),
 'oit':dict(priority=1,render='browser',catalog={'platform':'coursedog','home':'https://catalog.oit.edu/','path_prefix':'/programs/','min_depth':0,
   'program_lists':['https://catalog.oit.edu/programs']},policy=['https://www.oit.edu/academics/degrees','https://www.oit.edu/academics/degrees/nursing',
   'https://www.oit.edu/admissions/criteria','https://www.oit.edu/college-costs/scholarships/new-transfer-student/engineering-honors-scholarship']),
}
HOSTS={}
EXTRA_DISCOVER={'up':['https://www.up.edu/registrar/index.html','https://www.up.edu/academics/degrees-programs/index.html','https://up.smartcatalogiq.com/'],
 'wou':['https://wou.edu/registrar/','https://wou.edu/academics/'],'corban':['https://www.corban.edu/registrar/catalog/'],
 'warnerpacific-210304':['https://www.warnerpacific.edu/academics/registrar/academic-catalog/'],
 'bushnell':['https://bushnell.edu/academics/academic-support/registrar/academic-catalog/']}
DISCOVER={'TN':['trevecca','southern','lmunet','cumberland','fhu','king','milligan','bryan','maryvillecollege','sewanee','fisk','tusculum','tnwesleyan','bethelu','loc','johnsonu','welch','baptistu'],
 'OR':['wou','reed','pacificu','corban','bushnell','warnerpacific-210304','multnomah']}
PRI={'up':1,'georgefox':1,'sou':2,'wou':2,'eou':2,'osucascades':2,'willamette-210401':2,'lclark':2,'reed':2,'linfield':2,'pacificu':2,'cn':2,'trevecca':2,'southern':2,'lmunet':2,'sewanee':2,'maryvillecollege':2}
BLOCKED_EXTRA={'utk': ['https://advising.utk.edu/', 'https://www.utk.edu/academics/majors'], 'mtsu': ['https://www.mtsu.edu/advising/', 'https://www.mtsu.edu/programs/'], 'memphis': ['https://www.memphis.edu/advising/', 'https://www.memphis.edu/academics/'], 'etsu': ['https://www.etsu.edu/advisement/', 'https://www.etsu.edu/academics/'], 'utm': ['https://www.utm.edu/academics/majors-and-programs', 'https://www.utm.edu/offices/advising'], 'belmont': ['https://www.belmont.edu/academics/majors-programs/'], 'lipscomb': ['https://www.lipscomb.edu/academics'], 'leeuniversity': ['https://www.leeuniversity.edu/academics/']}
for k,v in BLOCKED_EXTRA.items(): TN[k]['policy']=TN[k]['policy']+v
for st,conf in (('TN',TN),('OR',OR)):
    r=reg(st); out=[]
    for folder,c in conf.items():
        i=r[folder]; out.append({'institution_key':i['institution_key'],'folder':folder,'name':i['name'],'control':i['control'],
          'domains':sorted(set(i['allowed_domains'])),'hosts':sorted({h for h in [c['catalog']['home'].split('/')[2]] if 'smartcatalogiq' in h or 'kuali' in h} | ({'catalog.oregonstate.edu'} if folder=='osucascades' else set())
          | ({'coursedog-pdfs-public-prod.s3.us-east-2.amazonaws.com'} if c['catalog'].get('platform')=='coursedog' else set())),'mode':'catalog',**c})
    for folder in DISCOVER[st]:
        i=r[folder]; d=i['domain']
        out.append({'institution_key':i['institution_key'],'folder':folder,'name':i['name'],'control':i['control'],'domains':sorted(set(i['allowed_domains'])),'hosts':[],
          'mode':'discover','priority':PRI.get(folder,3),'discover':[i['seeds']['website'],f'https://catalog.{d}/']+EXTRA_DISCOVER.get(folder,[]),'policy':[]})
        out[-1]['hosts']=HOSTS.get(folder,[])
    out.sort(key=lambda t:(t['priority'],t['name']))
    doc={'state':st,'purpose':'Program & Degree Deep Dive targets. Seeds are official hosts only; facts come only from fetched pages. '
         'mode=catalog targets have a reviewed catalog platform configuration; mode=discover targets are first crawled to locate their catalog.',
         'state_sources':[{'label':'THEC Academic Program Inventory','url':'https://thec.ppr.tn.gov/AcademicProgramInventorySearch','adapter':'thec_api'}] if st=='TN' else [],
         'institutions':out}
    (R/f'programs/targets/{st}.json').write_text(json.dumps(doc,indent=1)+'\n')
    print(st,len(out))
