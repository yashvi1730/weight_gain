import React,{Component} from 'react';


import './Footer.css';
//import './images/social_flat_rounded_rects_svg/Google+.svg';
//import './images/social_flat_rounded_rects_svg/Email.svg';
//import './images/social_flat_rounded_rects_svg/Facebook.svg';
//import './images/social_flat_rounded_rects_svg/LinkedIn.svg';
//import './images/social_flat_rounded_rects_svg/Twitter.svg';



import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faAngleDoubleRight,
  faBoxTissue,
  faAngleRight,
  faAngleLeft,
  faEnvelope,
  faUserMd,
} from "@fortawesome/free-solid-svg-icons";
import {
  fab,
  faFacebook,
  faFacebookF,
  faTwitter,
  faLinkedinIn,
  faWhatsapp,
} from "@fortawesome/free-brands-svg-icons";

class Footer extends Component {
    constructor(props){
        super(props)
        this.state = {
          a : 2,
        };
       
    }

   
    render(){
        return (
            <div style={{marginTop:"8%",backgroundColor:"white",paddingTop:"3%",paddingBottom:"5%"}}>
             
             
                <h1 className="sharetext" style={{color:"#163948"}}>Share now</h1>
                <p className="textbelowshare" style={{color:"#163948",paddingBottom:"1.5%"}}>Help your friends understand if they may be suffering from postpartum depression by sharing this online tool with them.</p>
               {/* <ul class="share-buttons" data-source="simplesharingbuttons.com" style={{textAlign:"center"}}>
                    <li><a href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F&quote=Proactive%E2%80%99s%20self-screening%20tool%20for%20PMDD%20provides%20a%20comprehensive%20assessment%20of%20your%20symptoms.%20Just%20answer%20few%20questions%20and%20get%20actionable%20insights!" title="Share on Facebook" target="_blank"><img alt="Share on Facebook" src={require("./images/social_flat_rounded_rects_svg/Facebook.svg")} /></a></li>
                    <li><a href="https://twitter.com/intent/tweet?source=http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F&text=Proactive%E2%80%99s%20self-screening%20tool%20for%20PMDD%20provides%20a%20comprehensive%20assessment%20of%20your%20symptoms.%20Just%20answer%20few%20questions%20and%20get%20actionable%20insights!:%20http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F" target="_blank" title="Tweet"><img alt="Tweet" src={require("./images/social_flat_rounded_rects_svg/Twitter.svg")} /></a></li>
                    <li><a href="https://plus.google.com/share?url=http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F" target="_blank" title="Share on Google+"><img alt="Share on Google+" src={require("./images/social_flat_rounded_rects_svg/Google+.svg")} /></a></li>
                    <li><a href="http://www.linkedin.com/shareArticle?mini=true&url=http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F&title=Proactive%E2%80%99s%20self-screening%20tool%20for%20PMDD%20provides%20a%20comprehensive%20assessment%20of%20your%20symptoms.%20Just%20answer%20few%20questions%20and%20get%20actionable%20insights!&summary=&source=http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F" target="_blank" title="Share on LinkedIn"><img alt="Share on LinkedIn" src={require("./images/social_flat_rounded_rects_svg/LinkedIn.svg")} /></a></li>
                    <li><a href="mailto:?subject=Proactive%E2%80%99s%20self-screening%20tool%20for%20PMDD%20provides%20a%20comprehensive%20assessment%20of%20your%20symptoms.%20Just%20answer%20few%20questions%20and%20get%20actionable%20insights!&body=:%20http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2FPMDD-tool%2F" target="_blank" title="Send email"><img alt="Send email" src={require("./images/social_flat_rounded_rects_svg/Email.svg")} /></a></li>
                </ul> 
               */}
               <div class="sharethis-inline-share-buttons"></div>
                <div className="d-flex justify-content-center">
              <a
                className="fb-share-button"
               
                href ="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fwww.proactiveforher.com%2Ftools%2Fpostpartum-depression-check%2F&quote=Proactive's%20PPD%20screening%20tool%20caters%20to%20all%20the%20new%20mothers%20facing%20mental%20struggle.%20It%20evaluates%20your%20responses%20to%20suggest%20a%20course%20of%20action%20and%20to%20help%20you%20understood%20your%20emotional%20"
                target="_blank"
                rel="noopener"
                aria-label=""
              >

                <FontAwesomeIcon
                  icon={faFacebookF}
                  className="b1"
                  style={{width:"50px"}}

                />
              </a>

              <a
                className="pl-4"
                href="https://twitter.com/intent/tweet/?text=Proactive's%20PPD%20screening%20tool%20caters%20to%20all%20the%20new%20mothers%20facing%20mental%20struggle.%20It%20evaluates%20your%20responses%20to%20suggest%20a%20course%20of%20action%20and%20to%20help%20you%20understood%20your%20emotional%20&amp;url=http%3A%2F%2Fproactiveforher.com%2Ftools%2Fpostpartum-depression-check%2F"
                
                target="_blank"
                rel="noopener"
                aria-label=""
              >
                <FontAwesomeIcon
                  icon={faTwitter}
                  className="b2"

                />
              </a>

              <a
                className="pl-4"
                href="mailto:?subject=Taking%20care%20of%20yourself%20is%20an%20essential%20part%20of%20motherhood.%20|%20Proactive%20&amp;body=Proactive's%20PPD%20screening%20tool%20caters%20to%20all%20the%20new%20mothers%20facing%20mental%20struggle.%20It%20evaluates%20your%20responses%20to%20suggest%20a%20course%20of%20action%20and%20to%20help%20you%20understood%20your%20emotional%20health%20http%3A%2F%2Fproactiveforher.com%2Ftools%2Fpostpartum-depression-check%2F"
                target="_self"
                rel="noopener"
                aria-label=""
              >
                <FontAwesomeIcon
                  icon={faEnvelope}
                  className="b3"

                />
              </a>
                                                                                                                                                                  
              <a                                                                                          
                className="pl-4"
                href="https://www.linkedin.com/shareArticle?mini=true&amp;url=http%3A%2F%2Fproactiveforher.com%2Ftools%2Fpostpartum-depression-check%2F&amp;title=Taking%20care%20of%20yourself%20is%20an%20essential%20part%20of%20motherhood.%20|%20Proactive%20&amp;summary=Proactive's%20PPD%20screening%20tool%20caters%20to%20all%20the%20new%20mothers%20facing%20mental%20struggle.%20It%20evaluates%20your%20&amp;source=http%3A%2F%2Fproactiveforher.com%2Ftools%2Fpostpartum-depression-check%2F"
                target="_blank"
                rel="noopener"
                aria-label=""
              >
                <FontAwesomeIcon
                  icon={faLinkedinIn}
                  className="b4"
                  style={{width:"50px"}}
                  />
              </a>

              <a
                className="pl-4"
                href="https://api.whatsapp.com/send?text=Proactive's%20PPD%20screening%20tool%20caters%20to%20all%20the%20new%20mothers%20facing%20mental%20struggle.%20It%20evaluates%20your%20responses%20to%20suggest%20a%20course%20of%20action%20and%20to%20help%20you%20understood%20your%20emotional%20health%20http%3A%2F%2Fproactiveforher.com%2Ftools%2Fpostpartum-depression-check%2F"
                target="_blank"
                rel="noopener"
                aria-label=""
              >
                <FontAwesomeIcon
                  icon={faWhatsapp}
                  className="b5"
                  style={{width:"50px"}}

                  />
              </a>
            </div>
            <div>
            <h1 className="sharetext2" style={{color:"#163948"}}>Comment</h1>
            <p style={{color:"#163948",paddingBottom:"1.5%"}}>Share anything you would like to say.</p>
            
            <div class="fb-comments" data-href="https://www.proactiveforher.com/tools/postpartum-depression-check/" data-numposts="20" data-width=""></div>
            </div>
             
            
             

            </div>
            

        )
    }


}



export default Footer;