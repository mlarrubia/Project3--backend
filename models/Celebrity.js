const mongoose = require('mongoose');
const Schema   = mongoose.Schema;


const celebritySchema = new Schema({
  name: {type: String, unique: true, required: true},
  youtubeHandle: String,
  instagramHandle: String,
  twitterHandle: String,
  image: String,
  category: {type: String},
  // category: {type: String, required: true},
  verified: Boolean,
  creator: {type: Schema.Types.ObjectId, ref: 'User'}
});

const Celebrity = mongoose.model('Celebrity', celebritySchema);

module.exports = Celebrity;