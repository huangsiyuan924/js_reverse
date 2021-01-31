var data = require('./data')



s = function (t) {
    var a, i, o = Math.abs(parseInt((new Date).getTime() * Math.random() * 1e4)).toString(), n = 0;
    for (a = 0; a < o.length; a++)
        n += parseInt(o[a]);
    return i = function(t) {
        return function(a, i) {
            return 0 >= i - "" + a.length ? a : (t[i] || (t[i] = Array(i + 1).join(0))) + a
        }
    }([]),
    n += o.length,
    n = i(n, 3 - n.toString().length),
    t.toString() + o + n
}
function get_r() {
    return s(1)
}

const express = require('express');
const bodyParser = require('body-parser');
// 创建应用实例
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.get('/get_r', function (req, res) {
    let r = get_r()
    res.json(
        {
            r: r
        }
    )
});
app.post('/get_qs', function (req, res) {
    let qs = JSON.stringify(data.u)
    res.json(
        {
            qs: qs
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


