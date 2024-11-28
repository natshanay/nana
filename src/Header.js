import React from 'react'
import './Header.css'
import Logo from './Logo'
import Find from './Find'
import Donate from './Donate'
import { Link } from 'react-router-dom'
import Login from './auth/Login'
const Header = () => {
  return (
    <div className='header'>
       <div className='div'>
       <div className='logo'>
          <Link to="/"> <Logo/></Link>
        </div>
        <div>
            <Find/>
        </div>
        <div>
            <Donate/>

        </div>
       </div>
     <div className='divv'>
     <div className='find-us-container'>
          
          <Link to="Login"><button className='find-us-btn'>Login</button>    </Link>    
  
      </div>
          <div className='find-us-container'>
          <Link to="signup"><button className='find-us-btn'>Sign up</button>    </Link>    
  
      </div>
     </div>

    </div>
  )
}

export default Header