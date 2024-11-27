import React from 'react'
import './Header.css'
import Logo from './Logo'
import Find from './Find'
import Donate from './Donate'
const Header = () => {
  return (
    <div className='header'>
        <div>
          <Logo/>
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