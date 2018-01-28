var request = require("request");



module.exports = (context, callback) => {
  var options = {
    method: 'GET',
    url: 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/',
    headers:
     {
       app_key: '64b0c95fb6a0ac6f0543f51afac40241',
       app_id: '7c6146c8',
       accept: 'application/json'
     }
   };
  options.url += context.http.headers.word;
  request(options, function (error, response, body) {
    if (error) throw new Error(error);
    const data = JSON.parse(body);
    const definition = data.results[0].lexicalEntries[0].entries[0].senses[0].definitions[0];
    callback(null, JSON.stringify(definition).slice(0, -1).substring(1));
  });

};
