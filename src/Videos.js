import React from 'react'
import './Videos.css'
import im from './logo.svg'
import { Link } from 'react-router-dom'
const Videos = ({hre,title,view}) => {

  return (
    <div className="videos"> 
   
       <Link to={hre}> <p>{title}</p></Link>
        <img src={im}/>
        <p>{view}</p>
    </div>
  )
}

export default Videos;