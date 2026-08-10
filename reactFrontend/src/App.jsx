import { useState, useEffect } from 'react'
import './App.css'
import TimelineContainer from './components/timelineContainer.jsx'
import { fetchAPI } from './services/client.js';

function App() {
  // eslint-disable-next-line no-unused-vars -- setTimelines is wired up by the backend fetch below
  const [timelines, setTimelines] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // useEffect(() => {
  // setTimelines([{ id: 1, number: 1, title: "Test Timelineddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd" }, { id: 2, number: 2, title: "Another" }, { id: 3, number: 4, title: "Abrother" }, { id: 4, number: 4, title: "Asister" }])
  // }, [])

  useEffect(() => {
    // TODO: fetch timelines from the backend (GET /timelines returns
    // an array of { number, title, id }) and call setTimelines(data).

    let isMounted = true;

    async function loadTimelines() {

      try {

        setLoading(true);
        const data = await fetchAPI('/timelines');
        if (isMounted) {
          setTimelines(data);
        }

      } catch (err) {
        if (isMounted){
          setError(err.message);
        }
      } finally {
        if (isMounted){
          setLoading(false);
        }
      }
    }

    loadTimelines();

    return () => {
      isMounted = false;
    };

  }, [])

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  const timelineContainers = timelines.map(timeline => 
    <TimelineContainer key={timeline.id} timeline={timeline} />
  )

  return (
    <div className="home">
      {/* <h1 className="title">Red String News</h1> */}
      <div className="timeline-grid">
        {timelineContainers}
      </div>
    </div>
  )
}

export default App
