
import About from './About';
import './App.css';
import Header from './Header';
import Hero from './Hero';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Landing from './Landing';
import Aboutus from './Aboutus';
import Empower from './Empower';
import Program from './Program';
import Herosec from './Herosec';

function App() {
  return (
    <BrowserRouter>
    <Header/>
    <Routes>

<Route path="/"
element={
  <>
  <About/>
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


      
  </Routes>
</BrowserRouter>
    
  );
}

export default App;
