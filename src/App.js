import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './screens/Home';
import About from './screens/About';
import NavBarElements from './components/Navbar/NavBarElements';


function App() {
  return (
   <Router>
    <NavBarElements />
      <Routes>
        <Route path='/' element = { <Home /> } />
        <Route path='/About' element = { <About /> } />
      </Routes>
   </Router>
  );
}

export default App;
