const ocrSpaceApi = require('ocr-space-api');

// Image file to upload
const imageFilePath = "test-image.jpg";

let options =  {
  apikey: '702bfefd7f88957',
  language: 'eng',
  imageFormat: 'image/png',
  isOverlayRequired: true
};

module.exports = (context, callback) => {
  ocrSpaceApi.parseImageFromLocalFile(imageFilePath, options).then(
    function (parsedResult) {
      parsedResult.parsedText = parsedResult.parsedText.replace(/(\r\n|\n|\r)/gm, "");
      callback(null, parsedResult.parsedText);
    }).catch(function (err) {
      callback(null, err);
    });
};
