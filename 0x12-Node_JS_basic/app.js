// https://nodejs.org/en/docs/guides/getting-started-guide/
// build our first web server
//  run your web server using node app.js. Visit http://localhost:3000 and you will see a message saying "Hello World".

const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
