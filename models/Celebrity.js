const mongoose = require('mongoose');
const Schema   = mongoose.Schema;


const celebritySchema = new Schema({
  name: String,
  youtubeHandle: String,
  instagramHandle: String,
  twitterHandle: String,
  verified: Boolean,
});

const Celebrity = mongoose.model('Celebrity', celebritySchema);

module.exports = Celebrity;