var fs = require('fs');

const testFolder = './pdfs';
// var pdfArray = [];
// fs.readdirSync(testFolder).forEach(file => {
// 	pdfArray.push(file);
// })
// console.log(pdfArray)

var path = require('path')
var extract = require('pdf-text-extract')

var path = require('path')


function convert(folder){
	return new Promise(function(resolve, reject){
		var pdfArray = [];
		fs.readdirSync(testFolder).forEach(pdf => {
			var filePath = path.join(__dirname, pdf);
			pdfArray.push(filePath);
		})
		resolve(pdfArray);
	}).then((pdfArray)=>{
		console.log("HERE "+ pdfArray[0])
		extract("./atbcoin_whitepaper.pdf", function(err, pages){console.log("YOYOYOYO", pages)})
		pdfArray.forEach((file)=>{
			extract(file, function (err, pages) {
			  if (err) {
			    console.dir("ERROR HERE~~~ ", err)
			    return
			  }
			  console.dir(pages)
			})
		})
	})
}

convert(testFolder)

// setTimeout(convert(pdfArray), 3000) 
//Omit option to extract all text from the pdf file 

