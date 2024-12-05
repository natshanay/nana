import React from 'react'
import './Header.css'
import Logo from './Logo'
import Find from './Find'
import Donate from './Donate'
import { Link } from 'react-router-dom'
import Search from './Search'
import Searchimage from './Searchimage'

const Header = () => {
  return (
    <div className='container'>
      <div>
      <Logo /> 
      </div>
      <div className='group-end'>
      <div>County Service</div>
      <div>Departments</div>
      <div>About the country</div>
<div>      <Searchimage/></div>
    <div>there is some thing to talk about here . . . .</div>
      </div>
      <div>
      </div>
       

    </div>
  )
}

export default Header