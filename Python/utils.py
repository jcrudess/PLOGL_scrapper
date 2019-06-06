import cx_Oracle as oracle 

def connect():
    dsn = oracle.makedsn('localhost', '1521', 'xe')
    conn = oracle.connect(user = 'PLOGL_scrapper', password = 'PLOGLscrapper11', dsn=dsn)

    c = conn.cursor()

    return c

def startLoad():
    c = connect()
    loadId = c.var(oracle.NUMBER)
    print('pozivam utility.p_start_load')
    c.callproc('utility.p_start_load', [loadId])
    loadIdRet = int(loadId.getvalue())
    return loadIdRet

def insertLink(link, loadID, module, sifra):
    c = connect()
    postoji = c.var(oracle.NUMBER)
    print('pozivam utility.p_insert_load_link')
    c.callproc('utility.p_insert_load_link', [link, loadID, module, sifra, postoji])
    print('uspješno završen poziv procedure')
    return int(postoji.getvalue())