import ollama

def test_timeline_consistency(past_events, current_event):
    # Your anchor events
    timeline_context = """
    Event 1: A US-brokered ceasefire agreement between Israel and Lebanon has been announced, contingent on Hezbollah ceasing attacks and withdrawing from southern Lebanon. However, Hezbollah—which was excluded from negotiations—has rejected the deal, with leader Naim Qassem characterizing it as "surrender" rather than a genuine peace agreement. Israel's defense minister stated the military will continue operations and remain in southern Lebanon, while residents face warnings against returning home. The fragile agreement's viability remains in serious doubt, as fighting has continued despite the accord and Iran has tied its own ceasefire negotiations to Lebanon's situation.
    Event 2: Israeli airstrikes in southern Lebanon killed nine people, including three military personnel, days after a ceasefire agreement was announced, prompting Lebanese leaders to denounce the attacks as violations of sovereignty. Meanwhile, Lebanon's parliament is advancing a sweeping amnesty law that would release thousands of detainees and reduce sentences for convicted militants, though it has sparked controversy among families of fallen soldiers who oppose pardoning those who killed their loved ones. The amnesty, the largest since Lebanon's civil war ended in 1990, reflects the country's complex sectarian divisions, with different political factions using it as a bargaining tool for their respective constituencies. As one lawmaker noted, "The draft law has entered the road of political bargains," highlighting how Lebanon's deep political divisions continue to shape major legislative efforts even amid ongoing regional conflict.
    Event 3: Following the downing of a U.S. Apache helicopter over the Strait of Hormuz, the United States and Iran engaged in an intense cycle of retaliatory strikes. The U.S. military conducted multiple waves of attacks on Iranian air defense systems and radar sites, which it described as "a proportional response," while Iran's Revolutionary Guards retaliated by launching drone and missile strikes against American military bases in Bahrain, Jordan, and Kuwait. Iran's Foreign Minister issued a stark warning, stating the country "will leave no attack or threat unanswered" and demanding foreign forces depart the region. The escalation further undermined ongoing peace negotiations between the two nations, with mediators struggling to bridge significant gaps over issues including Iran's uranium stockpile and sanctions relief.
    """

    # The test story
    new_story = """Israeli forces have intensified military operations in southern Lebanon, killing at least 17 people in recent strikes across multiple towns and cities, while Hezbollah continues to respond with attacks on Israeli troops. Despite a US-brokered ceasefire agreement announced in April, fighting has persisted, with Iran complicating negotiations by demanding that any peace deal address both the Lebanon and Iran conflicts. Former Israeli Prime Minister Ehud Barak, who withdrew troops from Lebanon in 2000, has warned that "there is no way to completely defeat Hezbollah without conquering the whole of Lebanon, which is totally impractical," arguing for a political solution rather than prolonged military occupation. The conflict has displaced nearly one million Lebanese civilians and killed over 3,600 people, while UN investigators have been sent to examine potential war crimes committed by all sides."""

    # A strict system prompt that changes the model's baseline behavior
    system_instruction = (
        "You are a strict, cynical database gatekeeper. Your job is to prevent unrelated news stories "
        "from contaminating a specific, highly focused historical timeline. You default to 'NO' "
        "unless there is explicit, undeniable proof of a direct connection."
    )

    # A highly structured user prompt enforcing gatekeeping criteria
    user_prompt = f"""
    You are evaluating a New Story to see if it qualifies to be added to an existing historical timeline.

    EXISTING TIMELINE:
    ---
    {timeline_context}
    ---

    NEW STORY TO EVALUATE:
    "{new_story}"

    CRITICAL GATEKEEPING CRITERIA:
    To output a DECISION of "YES", the New Story MUST meet at least one of these conditions:
    1. It explicitly names the specific core entities from the timeline (e.g., "ChronoCorp", "Project Hourglass").
    2. It directly impacts, results from, or causes the specific events mentioned in the timeline.

    If the New Story is simply about a broad, general topic (like "AI", "technology", or "computers") but does not involve the specific actors or plotline of the existing timeline, it is a CONTAMINATION. You must reject it.

    You must output your response in this exact format:

    CRITERIA CHECK 1 (Entity Match): [Does the story name specific entities from the timeline? Yes/No]
    CRITERIA CHECK 2 (Causal Link): [Does this story directly impact or stem from the timeline's specific events? Yes/No]
    
    DECISION: [Strictly "YES" or "NO". Only output "YES" if at least one Criteria Check above is "Yes".]
    REASONING: [A 1-2 sentence explanation of your decision.]
    """

    try:
        print("Sending request to qwen3:8b (with strict gatekeeping)...\n")
        
        response = ollama.chat(
            model='qwen3:8b',
            messages=[
                {'role': 'system', 'content': system_instruction},
                {'role': 'user', 'content': user_prompt}
            ],
            think = False,
            options={
                'temperature': 0.0, # Complete determinism
            }
        )
        
        print("--- TEST RESULT ---")
        print(response['message']['content'])
        print("-------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_timeline_consistency()