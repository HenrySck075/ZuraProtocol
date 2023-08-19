
from . import _ok as base

class CSS(base.sendhelp):

    method_AddRule:str
    method_CollectClassNames:str
    method_CreateStyleSheet:str
    method_Disable:str
    method_Enable:str
    method_ForcePseudoState:str
    method_GetBackgroundColors:str
    method_GetComputedStyleForNode:str
    method_GetInlineStylesForNode:str
    method_GetMatchedStylesForNode:str
    method_GetMediaQueries:str
    method_GetPlatformFontsForNode:str
    method_GetStyleSheetText:str
    method_SetEffectivePropertyValueForNode:str
    method_SetKeyframeKey:str
    method_SetMediaText:str
    method_SetRuleSelector:str
    method_SetStyleSheetText:str
    method_SetStyleTexts:str
    method_StartRuleUsageTracking:str
    method_StopRuleUsageTracking:str
    method_TakeCoverageDelta:str
    method_GetLayersForNode:str
    method_SetContainerQueryText:str
    method_SetLocalFontsEnabled:str
    method_SetScopeText:str
    method_SetSupportsText:str
    method_TakeComputedStyleUpdates:str
    method_TrackComputedStyleUpdates:str

    event_FontsUpdated:str
    event_MediaQueryResultChanged:str
    event_StyleSheetAdded:str
    event_StyleSheetChanged:str
    event_StyleSheetRemoved:str

    type_CSSComputedStyleProperty:str
    type_CSSKeyframeRule:str
    type_CSSKeyframesRule:str
    type_CSSMedia:str
    type_CSSPositionFallbackRule:str
    type_CSSProperty:str
    type_CSSPropertyRegistration:str
    type_CSSPropertyRule:str
    type_CSSRule:str
    type_CSSStyle:str
    type_CSSStyleSheetHeader:str
    type_CSSTryRule:str
    type_FontFace:str
    type_FontVariationAxis:str
    type_InheritedPseudoElementMatches:str
    type_InheritedStyleEntry:str
    type_MediaQuery:str
    type_MediaQueryExpression:str
    type_PlatformFontUsage:str
    type_PseudoElementMatches:str
    type_RuleMatch:str
    type_RuleUsage:str
    type_SelectorList:str
    type_ShorthandEntry:str
    type_SourceRange:str
    type_StyleDeclarationEdit:str
    type_StyleSheetId:str
    type_StyleSheetOrigin:str
    type_Value:str
    type_CSSContainerQuery:str
    type_CSSLayer:str
    type_CSSLayerData:str
    type_CSSRuleType:str
    type_CSSScope:str
    type_CSSSupports:str
    type_Specificity:str

    def __init__(self):
        super().__init__()

    
