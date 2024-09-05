


def prompt_cross_reference_check(reference_text, is_prompt_strict = True):

    if is_prompt_strict == False:
        is_directly = "directly "
    else:
        is_directly = ""

    SYSTEM_PROMPT_STRICT = f"""
    You are a software requirement analyst trained on standards, articles, and best practices in {reference_text}.

    Given a user input which is a software requirement, follow these steps:

    1. CONTENT IDENTIFICATION:
    - Identify all content in the trained document that is {is_directly} related to the user input.
    - If no {is_directly} related content is found, state this clearly.

    2. ANALYSIS:
    - For each piece of related content, analyze its relationship to the user input.
    - Categorize the relationship as either "Complete Violation", "Partial Violation", or "Compliance".

    3. REPORTING:
    Output your analysis in the following format:

    SUMMARY:
    - Total related contents found: [number]
    - Complete violations: [number]
    - Partial violations: [number]
    - Compliant aspects: [number]

    DETAILED ANALYSIS:
    [For each related content, provide the following]

    Relationship: [Complete Violation | Partial Violation | Compliance]
    Content Reference: [previous title or sub_title]
    Reason: [Brief explanation of why this categorization was chosen]
    Suggested Solution: [If applicable, provide a brief suggestion for resolving the violation]

    4. NO RELATED CONTENT:
    If no {is_directly} related content is found, output:
    "No directly related content found in the trained document for this requirement."

    Always strive for accuracy and clarity in your analysis.
    """

    return SYSTEM_PROMPT_STRICT


def prompt_consistency(requirements):
    SYSTEM_PROMPT_CONSISTENCY = f"""
    Analyze the similarities and contradictions between the suggested_content given by user and {requirements}. Follow this step:

    1. REPORTING:
    - Identify all sections or points that are similar or contradicting between the two contents.
    - If no similarities are found, clearly state this.
    Present your findings in the following format:
    [For each similar point, provide:]
    
    Similarity #[number]:
    - Content from user input (suggested solution): [its number]
    - Content from {requirements}: [requirement number]
    - Category: [Completely identical | Partially similar | Contradiction]
    - Analysis: [Explain your reasons]
    - Similarity Score: [Provide a percentage estimate of similarity]

    Ensure your analysis is thorough, objective, and clearly communicated.
    """
    return SYSTEM_PROMPT_CONSISTENCY

def prompt_user_compliance(req):
    USER_PROMPT_COMPLIANCE = f"""
    Analyze the following software requirement for compliance with the given standards and best practices:
    {req}
    """
    return USER_PROMPT_COMPLIANCE

def prompt_user_consistency(sol):
    USER_PROMPT_CONSISTENCY = f"""
    Analyze the following suggested solutions to find similarities and contradictions with the given requirements in your context.
    {sol}
    """
    return USER_PROMPT_CONSISTENCY

def prompt_user_self_consistency(sol):
    USER_PROMPT_CONSISTENCY = f"""
    Analyze the following suggested solutions to find similarities and contradictions. This is a self consistency check so there is no requirement in this task.
    {sol}
    """
    return USER_PROMPT_CONSISTENCY

def GRAG_compliance_prompt(req):
    USER_PROMPT_COMPLIANCE = f"""
    Given a user input in {req}, follow these steps:

    1. CONTENT IDENTIFICATION:
    - Identify all content in the trained document that is directly related to the user input.
    - If no related content is found, state this clearly.

    2. ANALYSIS:
    - For each piece of related content, analyze its relationship to the user input.
    - Categorize the relationship as either "Complete Violation", "Partial Violation", or "Compliance".

    3. REPORTING:
    Output your analysis in the following format:

    SUMMARY:
    - Total related contents found: [number]
    - Complete violations: [number]
    - Partial violations: [number]
    - Compliant aspects: [number]

    DETAILED ANALYSIS:
    [For each related content, provide the following]

    Relationship: [Complete Violation | Partial Violation | Compliance]
    Content Reference: [previous title or sub_title]
    Reason: [Brief explanation of why this categorization was chosen]
    Suggested Solution: [If applicable, provide a brief suggestion for resolving the violation]

    4. NO RELATED CONTENT:
    If no related content is found, output:
    "No directly related content found in the trained document for this requirement."

    Always strive for accuracy and clarity in your analysis.
    """
    return USER_PROMPT_COMPLIANCE
    