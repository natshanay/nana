import React from 'react'
import './Header.css'
import Logo from './Logo'
import Find from './Find'
import Donate from './Donate'
import { Link } from 'react-router-dom'
const Header = () => {
  return (
    <div className='header'>
        <div>
          <Link to="/"> <Logo/></Link>
        </div>
        <div>
            <Find/>
        </div>
        <div>
            <Donate/>

        </div>

    </div>
  )
}

export default Header