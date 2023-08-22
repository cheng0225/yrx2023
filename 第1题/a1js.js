




function get_params(d) {
    var e = Date['now']()
        , f = a('crypto-js')
        , g = '666yuanrenxue66'
        , h = f['AES']['encrypt'](e + String(d), g, {
        'mode': f['mode']['ECB'],
        'padding': f['pad']['Pkcs7']
    })
    return {
        'page': String(d),
        'token': f['MD5'](h['toString']())['toString'](),
        'now': e
    }
}
console.log(get_params(1))
