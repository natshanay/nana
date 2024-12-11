import React from 'react'
import './Header.css'
import Logo from './Logo'
import { Link } from 'react-router-dom'
// import Find from './Find'
// import Donate from './Donate'
// import { Link } from 'react-router-dom'
// import Search from './Search'
// import Searchimage from './Searchimage'

const Header = () => {
  return (
    <div className='container'>
      <div>
      <Link to="/"><Logo /> </Link>
      </div>
      <div className='group-end'>
      
      <div>County Service</div>
      <div>Departments</div>
      <div>About the country</div>
      
   
      </div>
      <div>
      </div>
    </div>
  )
}

export default Header