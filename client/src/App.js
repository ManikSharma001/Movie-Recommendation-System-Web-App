import { BrowserRouter, Routes, Route } from 'react-router-dom'

// pages
import MainPage from './pages/MainPage'
import AboutMe from './pages/AboutMe'

// components
import TopToolbar from './components/TopToolbar'
import AboutMeToolbar from './components/AboutMeToolbar'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <TopToolbar />
        <AboutMeToolbar />
        <div className="pages">
          <Routes>
            <Route
              path = "/"
              element={<MainPage />}
            />
            <Route
              path = "/pages/AboutMe"
              element={<AboutMe />} 
            />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
