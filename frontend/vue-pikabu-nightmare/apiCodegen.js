const swaggerGen = require('swagger-vue')
const jsonData = require('../../specs/user-pn-specs-v1.json')
const fs = require('fs')
const path = require('path')

let opt = {
  swagger: jsonData,
  moduleName: 'api',
  className: 'api'
}
const codeResult = swaggerGen(opt)
fs.writeFileSync(path.join(__dirname, 'src/gen/userApi.js'), codeResult)
