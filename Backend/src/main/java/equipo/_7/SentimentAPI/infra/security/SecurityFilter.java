//package equipo._7.SentimentAPI.infra.security;
//
//import equipo._7.SentimentAPI.domain.user.UserRepository;
//import jakarta.servlet.FilterChain;
//import jakarta.servlet.ServletException;
//import jakarta.servlet.http.HttpServletRequest;
//import jakarta.servlet.http.HttpServletResponse;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
//import org.springframework.security.core.context.SecurityContextHolder;
//import org.springframework.stereotype.Component;
//import org.springframework.web.filter.OncePerRequestFilter;
//
//import java.io.IOException;

//@Component
//public class SecurityFilter extends OncePerRequestFilter {
//
//    @Autowired
//    private UserRepository userRepository;
//    @Autowired
//    private TokenService tokenService;
//
//    @Override
//    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
//        var token = recuperaToken(request);
//        if (token != null) {
//            var subject = tokenService.getSubject(token);
//            var user = userRepository.findAllByEmail(subject);
//            if (user != null) {
//                var auth = new UsernamePasswordAuthenticationToken(user, null, user.getAuthorities());
//                SecurityContextHolder.getContext().setAuthentication(auth);
//            }
//        }
//        filterChain.doFilter(request, response);
//    }
//
//    private String recuperaToken(HttpServletRequest request) {
//        var authToken = request.getHeader("Authorization");
//        if (authToken != null) {
//            return authToken.replace("Bearer ", "");
//        }
//        return null;
//    }
//}
