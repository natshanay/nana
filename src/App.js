import About from './About';
import './App.css';
import Header from './Header';
import Hero from './Hero';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Landing from './Landing';
import Aboutus from './Aboutus';
import Empower from './Empower';
import Program from './Program';
import Login from './auth/Login';
import SignUp from './auth/Signup';
import Herosection from './Herosection';
import Footer from './Footer';

function App() {
  return (
    <BrowserRouter>
    <Header/>
    <Routes>

<Route path="/"
element={
  <>
 
<Hero/>




  
  </>
}

/>
<Route path='/aboutus' element={
  <Aboutus/>
}/>
<Route path='/empower' element={
  <Empower/>
}/>
<Route path='/landing' element={

<Landing/>
}/>
<Route path='/programs' element={

<Program/>
}/>
<Route path='/login' element={

<Login/>
}/>
<Route path='/signup' element={

<SignUp/>
}/>

  </Routes>
  <Footer/>

</BrowserRouter>
    
  );
}

export default App;