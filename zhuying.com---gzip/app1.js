var moment = require('./moment.js')
var getNextIssueUrl = function (gameId, gameType) {
    //return "/mobile"+Tools.staticPath() + 'data/NextIssue.js?gameId=' + gameId + '&_' + Math.random();
    var intTime = parseInt(moment().diff('Sun Nov 26 2017 20:49:04 GMT+0800','s')/5);
    return '/mobile/star/data/NextIssue.do?_' + intTime + '&gameMark=' + gameType;
};


console.log(getNextIssueUrl("1", "2"));