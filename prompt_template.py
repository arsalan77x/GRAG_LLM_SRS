# Simple Input/Output prompt
def prompt_query_graph_I (requirement, req_type):
    PROMPT = f"""
    Given this {req_type} requirement: {requirement}

    Your task is to analyze the requirement for incompleteness and violations based on the reference material. Follow these steps:

    1. Incompleteness: Identify any highly crucial components or processes that are present in the reference but missing from the requirement.
    2. Violations: Identify any aspects of the requirement that contradict or deviate from the standards or best practices outlined in the reference.

    Output your analysis in the following format:

    SUMMARY:
    - Total incompleteness issues found: [number]
    - Total violations found: [number]

    DETAILED ANALYSIS:
    [For each issue found, provide the following information]

    Issue Type: [Incompleteness | Violation]
    Issue Title: [Title]
    Explanation: [Explain why this is an incompleteness or violation and based on what reference]
    Suggested Solution: [Provide a specific recommendation to address the issue, based on the reference material]

    If no issues are found, output:
    No incompleteness or violations detected. The requirement aligns with the standards and best practices in the reference material.
    """
    return PROMPT

# Chain-of-Thoughts 
def prompt_query_analysis(requirement, req_type):
    PROMPT = f"""
    Given this {req_type} requirement: {requirement}

    Your task is to analyze the requirement by breaking it down into its key components and processes.

    # Steps:
    1. Break down the given requirement into key components and processes.
    2. List these components and processes, briefly explaining their purpose.

    # Output Format:
    - Component: [Description]
    - Process: [Description]
    """
    return PROMPT

def prompt_query_review_and_comparison(requirement, components):
    PROMPT = f"""
    Given this requirement: {requirement}

    Components and Processes Identified:
    {components}

    Your task is to review the reference material and compare the identified components and processes.

    # Steps:
    1. Identify relevant sections in the reference material related to the requirement.
    2. Compare the components and processes against the essential elements found in the reference material.
    3. Focus only on major incompleteness or severe deviations that would compromise the requirement.

    # Output Format:
    - Component: [Description]
    - Relevant Reference Section: [Reference]
    - Major Deviations or incompleteness: [Description]
    """
    return PROMPT

def prompt_query_critical_deficiencies_and_assessment(deviations):
    PROMPT = f"""
    Based on the following major deviations or incompleteness identified:
    {deviations}

    Your task is to explain the critical deficiencies and assess their impact on the project.

    # Steps:
    1. Clearly explain the severe impact of any critical deficiencies on the project's success.
    2. Cite specific parts of the reference material that emphasize the necessity of the missing or violated elements.
    3. Provide a final assessment determining if any critical deficiencies pose a significant risk to the project.

    # Output Format:
    - Deficiency Type: [Incompleteness | Violation]
    - Deficiency: [Description]
    - Suggested Solution: [Explanation and reference citation]
    - Final Assessment: [Whether this poses a significant risk]
    """
    return PROMPT




# Total-of-Thoughts  Classification-based
def prompt_query_initial_breakdown(requirement, req_type):
    PROMPT = f"""
    Given this {req_type} requirement: {requirement}

    Task 1: Break the requirement into 3-4 key components and provide multiple interpretations for each.

    # Steps:
    1. Break the requirement into 3-4 key components.
    2. For each component, generate 3 possible interpretations or angles of analysis.
    
    # Output your analysis in this format:
    - Component: [Description]
    - Interpretations: [Interpretation 1, Interpretation 2, Interpretation 3]
    """
    return PROMPT

def prompt_query_exploration_voting(requirement, component, interpretations):
    PROMPT = f"""
    Component: {component}
    Requirement: {requirement}
    interpretations: {interpretations}
    Task 2: Analyze each interpretation for alignment, violation, and incompleteness with reference material, and assign an initial vote.

    # Steps:
    1. For each interpretation, explore:
        a) Alignment with the reference material
        b) Violations of the reference material
        c) Incompleteness compared to the reference material
        d) Potential ambiguities or edge cases

    2. Assign a preliminary vote (1-5) for each interpretation based on likelihood of deficiencies.

    # Output your analysis in this format:
    - Interpretation: [Description]
    - Alignment: [Analysis]
    - Violation: [Analysis]
    - Incompleteness: [Analysis]
    - Ambiguities: [Analysis]
    - Preliminary Vote: [1-5]
    """
    return PROMPT

def prompt_query_evaluation_selection(requirement, component, interpretations):
    PROMPT = f"""
    Component: {component}
    Requirement: {requirement}
    interpretations: {interpretations}
    Task 3: Select the top 2 interpretations based on the initial votes for further analysis.

    # Steps:
    1. Review the interpretations and their votes.
    2. Select the top 2 interpretations for a detailed deep dive.

    # Output your analysis in this format:
    - Selected Interpretation 1: [Description]
    - Selected Interpretation 2: [Description]
    """
    return PROMPT

def prompt_query_deep_dive_voting(requirement, component, selected_interpretations):
    PROMPT = f"""
    Component: {component}
    Requirement: {requirement}
    interpretations: {selected_interpretations}
    Task 4: Conduct a detailed comparison with reference material and provide refined voting based on analyses from three different perspectives (lenient, moderate, and strict).

    # Steps:
    1. Generate 3 independent analyses for each selected interpretation.
    2. Provide a refined vote (1-10) for each analysis:
        - Lenient Analyst: Lower scores unless glaring issues
        - Moderate Analyst: Weigh both evidence and risks
        - Strict Analyst: Detail-oriented, often spots minor deviations

    # Output your analysis in this format:
    - Interpretation: [Description]
    - Analyst 1 Vote: [1-10]
    - Analyst 2 Vote: [1-10]
    - Analyst 3 Vote: [1-10]
    - Final Vote: [1-10]
    - Explanation: [Summarize key points and justify the final vote]
    """
    return PROMPT

def prompt_query_synthesis_final_voting(requirement, component, deep_dive_results):
    PROMPT = f"""
    Component: {component}
    Requirement: {requirement}
    results: {deep_dive_results}
    Task 5: Synthesize insights from various analyses and provide a final vote on whether the component violates or is incomplete according to standards.

    # Steps:
    1. Combine insights from different branches of thought.
    2. Conduct a final vote (1-10) considering all analyses.

    # Output your analysis in this format:
    - Component: [Description]
    - Final Vote: [1-10]
    - Explanation: [Summarize key points from the analyses and justify the final vote]
    - Suggested Solution: [Why this is crucial or a violation, cite relevant reference]
    - Deficiencies Type: [Incompleteness | Violation]
    """
    return PROMPT
