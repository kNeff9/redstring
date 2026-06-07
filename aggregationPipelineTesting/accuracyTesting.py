from pipeline_functions.article_embedding import *
from pipeline_functions.cluster_summary import *
from news_objects.Story import *
from news_objects.Timeline import *
from database.similarity_screen import *
from database.timelines import *
from database.stories import *
import os

"""

In this file I am using synthetic data to test the accuracy of my timeline sorting pipeline

"""
# --- DAY 1 ---
day_1_stories = [
    "Aerospace startup HorizonX successfully rolled out its next-generation Boreas II rocket onto the launchpad early this morning. Engineers began final system checks and fuel loading in preparation for a scheduled orbital insertion test later this week. The mission aims to deploy a cluster of climate-monitoring micro-satellites into low Earth orbit. Public spectators have already begun gathering at the coastal viewing site despite overcast weather conditions.",
    "Global tech giant OmniCorp announced a massive breakthrough in consumer quantum computing during its annual keynote address. CEO Elena Vance demonstrated a prototype desktop unit capable of processing complex cryptographic algorithms in seconds. Industry analysts are calling it a massive leap forward, though they warn commercial availability is still years away. Competitors saw their stock prices dip slightly immediately following the live presentation.",
    "A massive category 3 hurricane, dubbed Storm Arlene, officially made landfall on the eastern coast of Florida midday Tuesday. Heavy downpours and sustained winds of 115 mph have already knocked out power to over two hundred thousand residents. Emergency management agencies have issued mandatory evacuation orders for low-lying coastal zones. Local officials urge everyone to shelter in place as emergency response teams pause operations due to dangerous conditions.",
    "Metropolitan zoologists celebrated a rare milestone today with the successful hatching of an endangered Philippine eagle chick. The veterinary team had been monitoring the delicate incubation process around the clock for the past two months. This marks the first successful captive birth of the species in North America in over a decade. Conservationists hope this achievement will boost public awareness and funding for global habitat preservation initiatives."
]

# --- DAY 2 ---
day_2_stories = [
    "Following yesterday's rollout, HorizonX was forced to scrub its Boreas II rocket launch at T-minus 14 minutes due to an unexpected sensor anomaly. Ground control detected a minor pressure fluctuation in the liquid oxygen supply line during the final terminal countdown sequence. The launch window has been closed for the day while engineering teams drain the propellants to inspect the faulty valve. The startup announced they will attempt the orbital test flight again in forty-eight hours.",
    "Anonymous whistleblowers from OmniCorp leaked internal documents alleging that yesterday's highly publicized quantum computing demo was entirely staged. The leaked files suggest the prototype unit was actually tethered to a hidden server array running standard silicon processors. Regulatory bodies have already launched an expedited inquiry into potential investor fraud and corporate manipulation. OmniCorp's public relations team has declined to comment on the validity of the documents.",
    "As Hurricane Arlene pushes further inland, catastrophic flash flooding has submerged major transit corridors and trapped dozens of residents in their homes. Rescue crews are utilizing high-water vehicles and helicopters to conduct emergency evacuations across three counties. The storm has weakened to a category 1, but meteorologists warn that the slow-moving system will continue dumping historic amounts of rain. The governor has formally requested a federal disaster declaration to expedite relief funds.",
    "The city's historic downtown library reopened its doors to the public today following an extensive two-year architectural renovation project. The upgraded facility now boasts state-of-the-art digital media labs, expanded community learning spaces, and upgraded climate control for archival preservation. Local residents queued around the block to glimpse the restored glass dome ceiling and check out books. A ribbon-cutting ceremony was hosted by the mayor to commemorate the milestone."
]

# --- DAY 3 ---
day_3_stories = [
    "Regulatory pressure on OmniCorp intensified this morning as the Securities and Exchange Commission opened a formal investigation into the company's quantum computing demonstration. Shares of the tech giant plummeted by nearly twenty percent as institutional investors began rapidly liquidating their positions. The board of directors convened an emergency closed-door meeting amid growing internal calls for the immediate resignation of CEO Elena Vance. Legal experts predict severe financial penalties if the fraud allegations are proven true.",
    "The federal government officially approved a major emergency declaration for regions devastated by the remnants of Hurricane Arlene. Though the storm has finally dissipated into a post-tropical depression, emergency crews face a massive grid infrastructure crisis with major power transmission lines destroyed. Clean drinking water distribution centers have been established at local high schools to assist displaced families. Initial economic assessments estimate the total property and structural damage to be in the billions.",
    "An international team of marine biologists discovered a vibrant, previously unknown coral reef system deep in the southern Pacific Ocean. The pristine ecosystem thrives at depths typically devoid of significant coral growth, challenging long-held marine science paradigms. Researchers utilized autonomous underwater vehicles to map the expansive structure and collect unique biological samples. Early analysis suggests the reef hosts dozens of marine species never before documented by modern science.",
    "Local transit authorities introduced a new fleet of fully autonomous, zero-emission electric buses to the city's busiest commuter routes today. The pilot program aims to reduce urban carbon emissions while improving transit punctuality through AI-optimized routing software. Passengers can ride the new smart buses free of charge during the initial two-week trial period. City planners will monitor passenger feedback and safety metrics before expanding the fleet next year."
]

# --- DAY 4 ---
day_4_stories = [
    "HorizonX achieved a historic milestone this afternoon as the Boreas II rocket successfully lifted off and reached its targeted low Earth orbit. The second launch attempt went flawlessly, with all first-stage telemetry showing perfect nominal performance prior to a clean stage separation. The payload of climate-monitoring micro-satellites was deployed successfully and has already begun transmitting initial data back to ground stations. Company leadership celebrated the triumph, solidifying their position in the competitive commercial aerospace market.",
    "In a stunning corporate shakeup, OmniCorp CEO Elena Vance officially resigned from her position effective immediately following the staged quantum demo scandal. The board of directors appointed chief operating officer Arthur Pendelton as interim chief executive to steer the company through the ongoing federal fraud investigations. Pendelton issued a public apology pledging total transparency and complete cooperation with regulatory authorities moving forward. Market analysts remain skeptical about the firm's long-term recovery prospects.",
    "Displaced residents began returning to their neighborhoods today as floodwaters from the historic storm finally started to recede. Local utility companies have deployed thousands of technicians to systematically rebuild the electrical grid and restore power to critical infrastructure. Community volunteers organized massive street-by-street cleanup drives to clear hazardous debris and fallen trees from residential roadways. While the immediate danger has passed, officials emphasize that the long-term rebuilding process will take months.",
    "A legendary avant-garde painter passed away peacefully at the age of ninety-four in her longtime home and studio in Santa Fe. Over her prolific six-decade career, she fundamentally reshaped modern abstract art with her bold use of geometric forms and vibrant color theory. Museums worldwide have already announced plans for retrospective exhibitions to honor her immense cultural legacy and artistic contributions. Collectors expect her remaining private works to fetch record breaking prices at upcoming autumn auctions."
]

h1 = ["A massive category 3 hurricane, dubbed Storm Arlene, officially made landfall on the eastern coast of Florida midday Tuesday. Heavy downpours and sustained winds of 115 mph have already knocked out power to over two hundred thousand residents. Emergency management agencies have issued mandatory evacuation orders for low-lying coastal zones. Local officials urge everyone to shelter in place as emergency response teams pause operations due to dangerous conditions.",
      "Global tech giant OmniCorp announced a massive breakthrough in consumer quantum computing during its annual keynote address. CEO Elena Vance demonstrated a prototype desktop unit capable of processing complex cryptographic algorithms in seconds. Industry analysts are calling it a massive leap forward, though they warn commercial availability is still years away. Competitors saw their stock prices dip slightly immediately following the live presentation."]

h2 = ["As Hurricane Arlene pushes further inland, catastrophic flash flooding has submerged major transit corridors and trapped dozens of residents in their homes. Rescue crews are utilizing high-water vehicles and helicopters to conduct emergency evacuations across three counties. The storm has weakened to a category 1, but meteorologists warn that the slow-moving system will continue dumping historic amounts of rain. The governor has formally requested a federal disaster declaration to expedite relief funds.",
      "Anonymous whistleblowers from OmniCorp leaked internal documents alleging that yesterday's highly publicized quantum computing demo was entirely staged. The leaked files suggest the prototype unit was actually tethered to a hidden server array running standard silicon processors. Regulatory bodies have already launched an expedited inquiry into potential investor fraud and corporate manipulation. OmniCorp's public relations team has declined to comment on the validity of the documents."]


article_clusters = get_article_clusters(day_4_stories)

stories = []

for cluster in article_clusters:

    newStory = Story(cluster.centroid, cluster.articles[0]) # Creating stories with accurate centroids from synthetic stories
    stories.append(newStory)

for s in stories:

    timeline_candidates = get_timeline_candidates(s)

    if len(timeline_candidates) == 0:

        new_timeline = Timeline(s.timeline_id, s.centroid, s.text[:10] + "...")

        insert_timeline(new_timeline)

        insert_story(s)

        continue


    for row in timeline_candidates:

        candidate_id = row[0]

        s.timeline_id = candidate_id

        insert_story(s)

        break


