import React from 'react'
import './Hero.css'
import { Link } from 'react-router-dom'
const Hero = () => {
  return (
    <div>
      <h1>Registrar of Voters</h1>
    <div className='nana' >
        <Link className='white' to="/"> Registor to Vote</Link>
        <Link className='white' to="/about"> Vote in Person</Link>
        <Link className='white' to="/desktop"> Vote by Mail</Link>
        <Link className='white' to="/go"> Get Involved</Link>
        <Link className='white' to="somehre">Elections</Link>
        <Link className='white' to="somehre">Notices</Link>

    </div>
      </div>
  )
}

export default Hero;