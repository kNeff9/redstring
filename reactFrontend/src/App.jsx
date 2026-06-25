import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="home">
      <h1 className="title">Red String News</h1>
    </div>
  )
}

export default App
