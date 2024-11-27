import React from 'react'
import './About.css'
// import { a } from "react-router-dom";
import Logo from './Logo';
const About = () => {
  return (
    <div>
        <div className='container'>
            <ul>
                <a href="/aboutus">About Us</a >
                <a href="/aboutus"><Logo/></a >
                <a href="/empower" >Empowering Girls</a > 
                <a href="/aboutus" >Programs</a >
                <a href="/aboutus" >About</a >
                <a href="/aboutus" >About</a >
                <a href="/aboutus" >About</a>
            </ul>
        </div>

    </div>
  )
}

export default About