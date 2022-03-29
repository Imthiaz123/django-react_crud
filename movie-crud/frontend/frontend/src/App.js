import './App.css'
import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import AddMovie from './components/AddMovie'
import Login from './components/login'

function App () {
  const [token, setToken] = useState('')

  const userLogin = tok => {
    setToken(tok)
  }

  return (
    <div className='App'>
      <Login userLogin={userLogin} />
      <AddMovie token={token} />
    </div>
  )
}

export default App
