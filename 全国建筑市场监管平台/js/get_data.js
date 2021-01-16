
const express = require('express');
const bodyParser = require('body-parser');
// 创建应用实例
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.get('/get_data', function (req, res) {
    // console.log(req.query["enc_data"])
    let result = get_data(req.query["enc_data"])
    res.json(
        {
            result: result
        }
    )
});
// 监听8000端口并在运行成功后向控制台输入服务器启动成功！
const server = app.listen(8000, function () {
    let host = server.address().address;
    let port = server.address().port;
    console.log(
        "node服务启动，监听地址为: http://%s:%s", host, port
    )
});



var CryptoJS = require("crypto-js");

f = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
m = CryptoJS.enc.Utf8.parse("0123456789ABCDEF");
function get_data(t) {
    var e = CryptoJS.enc.Hex.parse(t)
        , n = CryptoJS.enc.Base64.stringify(e)
        , a = CryptoJS.AES.decrypt(n, f, {
        iv: m,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
        , r = a.toString(CryptoJS.enc.Utf8);
    return r.toString()
}


