import React from 'react'
import './About.css'
import { BrowserRouter, Link } from "react-router-dom";
import Logo from './Logo';
const About = () => {
  return (
    <>
        <div className='container'>
            <ul>
                <Link to="/aboutus">About Us</Link >
                
                <Link to="/empower" >Empowering Girls</Link > 
                <Link to="/programs" >Progrmas</Link >
                <Link to="/news" >News</Link >
                <Link to="/landing" >Landing</Link >
              
            </ul>
        </div>

    </>
  )
}

export default About