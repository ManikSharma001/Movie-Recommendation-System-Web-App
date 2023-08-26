// Homepage

// Components
import InputBox from '../components/InputBox'
import Explainer from '../components/Explainer'
import MovieRecommendation from '../components/MovieRecommendation'

const MainPage = () => {
	// Movies sent to backend via InputBox.js

	return (
		<div className="mainpage">
			<Explainer />
				<div className="Input">
					<InputBox />
				</div>
		</div>
	)
}

export default MainPage;