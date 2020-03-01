const path = require('path');

module.exports = {
// relative to the folder provided by outputDir
  assetsDir: '../static',
  publicPath: '',
// outputDir: location of build index.html file of vue; should hold other js files
  outputDir: path.resolve(__dirname, '../../flask-vue/templates'),
  runtimeCompiler: undefined,
  productionSourceMap: undefined,
  parallel: undefined,
  css: undefined,

  pages: {
    index: {
      entry: "src/main.js",
      template: "src/template/index.html",
      filename: "index.html",
      title: "Home"
    }
  }
};