const express = require('express');
const bodyParser = require('body-parser');
// 创建应用实例
const app = express();
pp.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.get('/get_data', function (req, res) {
    let anti_result = o()()["messagePackSync"]("http://yangkeduo.com/search_result.html");

    res.json(
        {
            anti_result: anti_result
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