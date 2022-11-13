import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import  Footer  from './components/Footer';
import  Header  from './components/Header';
import  HomePage from './pages/HomePage';

import PropertiesPages from './pages/PropertiesPage';

function App() {
  return (
    <>
      <Router>
          <Header/>
          <main className='py-3'>
            <Routes>
              <Route path='/' element={<HomePage/>} ></Route>
            </Routes>
            <Routes>
                <Route path='/properties' element={<PropertiesPages/>}>

                </Route>
            </Routes>
          </main>
      </Router>
      <ToastContainer/>
      <Footer/>
    </>
  );
}

export default App;
