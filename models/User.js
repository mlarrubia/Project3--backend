const mongoose = require('mongoose');
const Schema   = mongoose.Schema;


const userSchema = new Schema({
    username: String,
    password: String,
    type: String,
  //   image: 
});

const User = mongoose.model('User', userSchema);

module.exports = User;