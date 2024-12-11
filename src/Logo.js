import React from 'react'
import './Logo.css'
import img from "./assets/img/chris-kursikowski-ze5wHM9kplc-unsplash.jpg"
const Logo = () => {
  return (
    <div className='logosh'>
        <span  ><img className='logo' src={img}/> </span>
        

    </div>
  )
}

export default Logo