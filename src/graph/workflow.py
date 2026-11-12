from langgraph.graph import StateGraph, START, END
from src.schemas import ScreeningState
from src.graph.nodes import analyze_node,score_node,route_validation,retry_node
def build_graph():
    g=StateGraph(ScreeningState)
    g.add_node("analyze",analyze_node); g.add_node("retry",retry_node); g.add_node("score",score_node)
    g.add_edge(START,"analyze")
    g.add_conditional_edges("analyze",route_validation,{"retry":"retry","score":"score"})
    g.add_edge("retry","analyze"); g.add_edge("score",END)
    return g.compile()
