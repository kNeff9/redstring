import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { fetchAPI } from '../services/client.js'
import '../css/timeline.css'

function formatDate(value) {
  if (!value) return ''
  const parsed = new Date(value)
  if (Number.isNaN(parsed.getTime())) return value
  return parsed.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}

function Timeline() {
  const { timelineId } = useParams()
  const [stories, setStories] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let isMounted = true

    async function loadStories() {
      try {
        setLoading(true)
        const data = await fetchAPI(`/timelines/${timelineId}`)
        if (isMounted) {
          // Accept either a raw array of stories or an object wrapping them.
          setStories(Array.isArray(data) ? data : data?.stories ?? [])
        }
      } catch (err) {
        if (isMounted) {
          setError(err.message)
        }
      } finally {
        if (isMounted) {
          setLoading(false)
        }
      }
    }

    loadStories()

    return () => {
      isMounted = false
    }
  }, [timelineId])

  return (
    <main className="timeline-page">
      <Link to="/" className="back-link" aria-label="Back to timelines">
        <svg
          className="back-icon"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
          focusable="false"
        >
          <line x1="20" y1="12" x2="4" y2="12" />
          <polyline points="11 5 4 12 11 19" />
        </svg>
      </Link>

      {loading && <p className="timeline-status">Loading stories...</p>}
      {error && <p className="timeline-status">Error: {error}</p>}

      {!loading && !error && stories.length === 0 && (
        <p className="timeline-status">No stories found for this timeline.</p>
      )}

      {!loading && !error && stories.length > 0 && (
        <ul className="story-list">
          {stories.map((story, index) => (
            <li key={story.id ?? index} className="story-item">
              <article className="story-card">
                <time className="story-date">{formatDate(story.date)}</time>
                {/* {story.num != null && (
                  <span className="story-number">{story.num}</span>
                )} */}
                <p className="story-content">{story.content}</p>
              </article>
            </li>
          ))}
        </ul>
      )}
    </main>
  )
}

export default Timeline
