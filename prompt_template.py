# Simple Input/Output prompt
def prompt_IO (requirement, reference_text):
    PROMPT = f"""
    Requirement: {requirement}

    Reference Text: {reference_text}

    Assess whether the requirement aligns with the reference text. Follow these steps:
    1. Identify if the requirement is fully addressed in the reference text.
    2. Determine if there are any inconsistencies or violations in the requirement with respect to the reference text.
    3. If the requirement conforms, state "Conforms."
    4. If the requirement violates or contradicts the reference text, state "Violates" and briefly explain why.

    Output your assessment in the following format:
    - Assessment: [Conforms | Violates]
    - Explanation: [Provide a concise explanation of your assessment.]
    """

    return PROMPT

# Chain-of-Thoughts 
def prompt_CoT_1(requirement, reference_text):
    PROMPT = f"""
        Requirement: {requirement}

        Reference Text: {reference_text}

        Break down the components of the requirement and the reference text into the following formal logical structure:
        1. **Purpose**: What is the objective or goal of the requirement or reference text?
        2. **Action**: What specific actions or processes are described?
        3. **Conditions/Constraints**: What conditions or constraints must be satisfied for the actions to occur?

        Output the results in this format:
        - **Requirement Components**:
        - Purpose: [Requirement's purpose]
        - Action: [Requirement's action]
        - Conditions/Constraints: [Requirement's conditions/constraints]

        - **Reference Text Components**:
        - Purpose: [Reference text's purpose]
        - Action: [Reference text's action]
        - Conditions/Constraints: [Reference text's conditions/constraints]
        """
    return PROMPT

def prompt_CoT_2(
    Requirement_Purpose, 
    Requirement_Action, 
    Requirement_Conditions_Constraints, 
    Reference_Text_Purpose, 
    Reference_Text_Action, 
    Reference_Text_Conditions_Constraints
):
    PROMPT = f"""
    The following are the extracted components of the requirement and the reference text:

    - **Requirement Components**:
    - Purpose: {Requirement_Purpose}
    - Action: {Requirement_Action}
    - Conditions/Constraints: {Requirement_Conditions_Constraints}

    - **Reference Text Components**:
    - Purpose: {Reference_Text_Purpose}
    - Action: {Reference_Text_Action}
    - Conditions/Constraints: {Reference_Text_Conditions_Constraints}

    Compare the corresponding components (Purpose vs. Purpose, Action vs. Action, Conditions/Constraints vs. Conditions/Constraints) and provide an analysis for each:

    1. **Purpose Comparison**: Describe whether the purposes align, partially align, or conflict. Highlight any key differences or overlaps.
    2. **Action Comparison**: Identify whether the actions align, partially align, or conflict. Explain any inconsistencies or missing elements.
    3. **Conditions/Constraints Comparison**: Assess whether the conditions or constraints are consistent. Note any contradictions, gaps, or additional requirements.

    Output your analysis in the following format:
    - **Purpose Analysis**: [Analysis of alignment or conflict]
    - **Action Analysis**: [Analysis of alignment or conflict]
    - **Conditions/Constraints Analysis**: [Analysis of alignment or conflict]
    """
    return PROMPT


def prompt_CoT_3(Purpose_Analysis, Action_Analysis, Alignment_Analysis):
    PROMPT = f"""
    The following is the analysis of the components from the requirement and the reference text:

    - **Purpose Analysis**: {Purpose_Analysis}
    - **Action Analysis**: {Action_Analysis}
    - **Conditions/Constraints Analysis**: {Alignment_Analysis}

    Based on the component analyses, determine whether the requirement conforms to or violates the reference text by considering the following:
    1. Does the Purpose align overall with the reference text?
    2. Are the Actions described in the requirement consistent with the reference text?
    3. Do the Conditions/Constraints fully align, partially align, or conflict with the reference text?

    Provide your overall assessment and rationale in this format:
    - **Overall Assessment**: [Conforms | Violates]
    - **Rationale**: [Explain why the requirement conforms or violates based on the component analyses. Highlight key areas of alignment or conflict.]
    """
    return PROMPT





# Total-of-Thoughts  Classification-based
def prompt_ToT_1(requirement, reference_text):
    PROMPT = f"""
    You are a set of three reasoning agents (Agent A, Agent B, Agent C), followed by a final Arbiter. Your goal is to break down the given requirement and the reference text into logical components.

    **Instructions for Agents:**
    - Each agent should work independently and not share or alter their reasoning based on the others.
    - Each agent should provide a breakdown for both the requirement and the reference text into:
    - Purpose
    - Action
    - Conditions/Constraints

    **Given Input:**
    - Requirement: {requirement}
    - Reference Text: {reference_text}

    **Format for Each Agent's Response:**
    - **Agent [Name] Analysis**:
    - **Requirement Components**:
        - Purpose: ...
        - Action: ...
        - Conditions/Constraints: ...
    - **Reference Text Components**:
        - Purpose: ...
        - Action: ...
        - Conditions/Constraints: ...

    **Steps:**
    1. Agent A, provide your breakdown.
    2. Agent B, provide your breakdown.
    3. Agent C, provide your breakdown.

    After all agents have provided their breakdowns:

    **Arbiter Instructions:**
    - Review all three agents' analyses.
    - Compare and identify the most accurate or comprehensive elements.
    - Produce a final, consolidated breakdown that selects the best Purpose, Action, and Conditions/Constraints for both the requirement and the reference text.

    **Final Output Format (Arbiter's Consolidated Answer):**
    - **Final Consolidated Components**:
    - **Requirement Components**:
        - Purpose: [Consolidated Purpose]
        - Action: [Consolidated Action]
        - Conditions/Constraints: [Consolidated Conditions/Constraints]

    - **Reference Text Components**:
        - Purpose: [Consolidated Purpose]
        - Action: [Consolidated Action]
        - Conditions/Constraints: [Consolidated Conditions/Constraints]
    """
    return PROMPT

def prompt_ToT_2(final_consolidated_breakdown):
    PROMPT = f"""
    You are a set of three reasoning agents (Agent A, Agent B, Agent C), followed by a final Arbiter. You have received a final consolidated breakdown of the requirement and reference text from the previous step.

    **Consolidated Breakdown**:
    {final_consolidated_breakdown}

    **Instructions for Agents:**
    - Each agent should independently analyze how the Purpose, Action, and Conditions/Constraints of the requirement compare to those of the reference text.
    - Identify if each component aligns, partially aligns, or conflicts.
    - Provide reasoning for each comparison.

    **Format for Each Agent's Response**:
    - **Agent [Name] Analysis**:
    - **Purpose Analysis**: [Describe alignment/conflict and reasons]
    - **Action Analysis**: [Describe alignment/conflict and reasons]
    - **Conditions/Constraints Analysis**: [Describe alignment/conflict and reasons]

    **Steps**:
    1. Agent A, provide your analysis.
    2. Agent B, provide your analysis.
    3. Agent C, provide your analysis.

    **Arbiter Instructions:**
    - Review all three agents' analyses.
    - Identify the strongest reasoning for each component comparison.
    - Produce a final, synthesized analysis that captures the most accurate and insightful points raised by the agents.

    **Final Output Format (Arbiter's Consolidated Analysis)**:
    - **Purpose Analysis**: [Consolidated Analysis]
    - **Action Analysis**: [Consolidated Analysis]
    - **Conditions/Constraints Analysis**: [Consolidated Analysis]
    """
    return PROMPT

def prompt_ToT_3(consolidated_analysis):
    PROMPT = f"""
    You are a set of three reasoning agents (Agent A, Agent B, Agent C), followed by a final Arbiter. You have received a consolidated comparison analysis from the previous step.

    **Consolidated Analysis**:
    {consolidated_analysis}

    **Instructions for Agents:**
    - Each agent independently determines whether the requirement overall "Conforms" or "Violates" the reference text.
    - Consider:
    1. Purpose Alignment
    2. Action Consistency
    3. Conditions/Constraints Alignment

    **Format for Each Agent's Response**:
    - **Agent [Name] Final Assessment**:
    - Overall Assessment: [Conforms | Violates]
    - Rationale: [Explain reasoning based on previous consolidated analysis]

    **Steps**:
    1. Agent A, provide your final assessment.
    2. Agent B, provide your final assessment.
    3. Agent C, provide your final assessment.

    **Arbiter Instructions:**
    - Review the three agents' assessments.
    - Consider which assessment is best supported by the prior analyses.
    - Produce a final determination and rationale that either adopts one agent’s perspective entirely or synthesizes them if needed.

    **Final Output Format (Arbiter's Conclusion)**:
    - **Overall Assessment**: [Conforms | Violates]
    - **Rationale**: [Detailed explanation incorporating the best reasoning points from the agents]
    """
    return PROMPT
