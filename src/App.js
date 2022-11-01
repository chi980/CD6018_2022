import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './screens/Home';
import Login from './screens/Login';
import NavBarElements from './components/Navbar/NavBarElements';


function App() {
  return (
   <Router>
    <NavBarElements />
      <Routes>
        <Route path='/' element = { <Home /> } />
        <Route path='/Login' element = { <Login /> } />
      </Routes>
   </Router>
  );
}

export default App;
