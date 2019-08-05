const mongoose = require('mongoose');
const Schema   = mongoose.Schema;


const userSchema = new Schema({
    username: String,
    password: String,
    type: String,
    // celebrities: [{type: Schema.Types.ObjectId, ref: "Celebrity"}],

  //   image: 
});

const User = mongoose.model('User', userSchema);

module.exports = User;