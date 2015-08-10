/* eslint-disable */
var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

var APP_ENV = process.env.APP_ENV || "development";

var buildCssLoaders = function() {
  var cssLoader = APP_ENV === "development"
    ? "css?modules&sourceMap&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]"
    : "css?modules";

  var loaders = [
    cssLoader,
    "autoprefixer?browsers=last 2 version",
    "sass?indentedSyntax",
  ]

  return [
    ExtractTextPlugin.extract(
      "style",
      loaders.join("!")
    )
  ];
};

var buildJsLoaders = function() {
  if (APP_ENV === "development") {
    return [
      "react-hot",
      "babel?optional[]=runtime&stage=0&cacheDirectory"
    ];
  } else {
    return [
      "babel?optional[]=runtime&stage=0"
    ];
  }
};

var devPlugins = [
  new ExtractTextPlugin("[name].css"),
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(),
  new webpack.DefinePlugin({
    "process.env": {
      APP_ENV: JSON.stringify(APP_ENV),
    }
  }),
  new BundleTracker({filename: './webpack-stats.json'})
];

var prodPlugins = [
  new ExtractTextPlugin("[name]-[hash].css"),
  new webpack.IgnorePlugin(/\.\/dev/, /\/config$/),
  new webpack.DefinePlugin({
    "process.env": {
      APP_ENV: JSON.stringify(APP_ENV),
    }
  }),
  new webpack.optimize.UglifyJsPlugin({
    souceMap: false,
    compress: {
      warnings: false,
    },
  }),
  new BundleTracker({filename: './webpack-stats.json'})
];

var config = {
  // context: __dirname,

  devtool: (APP_ENV === "development" ? "eval-cheap-module-source-map" : null),

  entry: {
    app: './aggregator/static/js/index.js',
  },

  output: {
    path: path.resolve('./aggregator/static/bundles/'),
    filename: APP_ENV === "development" ? '[name].js' : '[name]-[hash].js',
  },

  module: {
    loaders: [
      {
        test: /\.css$/,
        loaders: ["css"],
      },
      {
        test: /\.sass$/,
        loader: ExtractTextPlugin.extract("style", "css?modules!autoprefixer?browsers=last 2 version!sass?indentedSyntax"),
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loaders: buildJsLoaders(),
      },
      {
        test: /\.(jpe?g|png|gif|svg|ico)($|\?)/,
        loaders: ["url?limit=10000"],
      },
      // {
      //   test: /\.woff2?($|\?)/,
      //   loaders: ["url?limit=100000"],
      // },
      // {
      //   test: /\.(ttf|eot)($|\?)/,
      //   loaders: ["file"],
      // },
    ],
  },

  plugins: (APP_ENV === "development" ? devPlugins : prodPlugins),

  resolve: {
    // Only allow ".js" to be appended automatically when resolving (e.g.
    // `import foo from "./bar"` will find `./bar.js`), everything else must
    // be specified with the full extension, e.g. `import styles from
    // "./bar.sass"`
    extensions: ["", ".js"],

    // When resolving module paths (i.e. non-absolute and non-relative, e.g.
    // `import foo from "blah/foo"`), webpack will look in these dirs and any
    // parent dirs above it with the same names (e.g. `./blah`, `../blah`,
    // `../../blah`, etc).
    modulesDirectories: ["src", "node_modules"],
  },

};

// console.log("loaders", config.module.loaders);

module.exports = config;
