import { Link } from "react-router-dom"
import "../css/timelineContainer.css"

function TimelineContainer({ timeline }) {
  return (
    <Link to={`/timelines/${timeline.id}`} className="timeline-container-link">
      <article className="timeline-container">
        <h2 className="timeline-container-title">{timeline.title}</h2>
      </article>
    </Link>
  )
}

export default TimelineContainer
