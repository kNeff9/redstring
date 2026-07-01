import "../css/timelineContainer.css"

function TimelineContainer({ timeline }) {
  return (
    <article className="timeline-container">
      <h2 className="timeline-container-title">{timeline.title}</h2>
    </article>
  )
}

export default TimelineContainer
