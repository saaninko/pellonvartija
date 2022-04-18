
const http = require('http');
const fs = require('fs');

const requestListener = function (req, res) {
  res.writeHead(200);
  try {
    const data = fs.readFileSync('/home/eyeofthefieldbeholder/pellonvartija/data/data.txt', 'utf8');
    console.log('File read');
    res.end(data);
    } catch (err) {
    console.error(err);
    }

}

const server = http.createServer(requestListener);
server.listen(7234);
