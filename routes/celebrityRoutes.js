const express     = require('express');
const router      = express.Router();

const User        = require('../models/User');
const Celebrity        = require('../models/Celebrity');

// The post route might be a little off
router.post('/', (req, res, next)=>{

    console.log(req.body);
    Celebrity.create({
        name: req.body.name,
        youtubeHandle: req.body.youtube,
        instagramHandle: req.body.instagram,
        twitterHandle: req.body.twitter,
        image: req.body.image,
        category: req.body.category,
        verified: false,
        creator: req.user._id,
    })
    .then(()=>{
     
    })
    .catch((err)=>{
    //   res.json(err);
    })


  })

  module.exports = router;