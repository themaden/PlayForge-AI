class MRAIDNetworkHandler:
    """Provides SDK bridges for Meta Ads (FbPlayable), TikTok Pangle, Google AC, and Unity MRAID 3.0."""

    @staticmethod
    def get_network_snippet(network_name: str) -> str:
        if network_name.lower() == "meta":
            return """
            // Meta (Facebook) Playable Ad API
            window.FbPlayable = window.FbPlayable || {
                handleClick: function() {
                    console.log("[Meta Playable] CTA Clicked");
                    if (typeof FbPlayable !== 'undefined' && FbPlayable.handleClick) {
                        FbPlayable.handleClick();
                    }
                }
            };
            """
        elif network_name.lower() == "tiktok":
            return """
            // TikTok Pangle Playable SDK
            window.playableSDK = window.playableSDK || {
                openAppStore: function() {
                    console.log("[TikTok Pangle] openAppStore triggered");
                    if (window.playableSDK && window.playableSDK.openAppStore) {
                        window.playableSDK.openAppStore();
                    }
                }
            };
            """
        else:
            return """
            // MRAID 3.0 Standard Protocol
            function triggerMraidCTA() {
                if (window.mraid && window.mraid.open) {
                    window.mraid.open();
                } else {
                    console.log("[MRAID] Store Redirect triggered");
                }
            }
            """
